"""
GitHub Integration Module for EIDOLON-7
Monitors hw9-issues repository and responds to mentions
"""

import os
import requests
from typing import List, Dict, Optional
from datetime import datetime


class GitHubIssueMonitor:
    """
    Monitor GitHub issues and respond when EIDOLON-7 is mentioned
    
    This service watches the cs320f25/hw9-issues repository and responds
    to issues that specifically mention EIDOLON-7 by name.
    """
    
    def __init__(self, github_token: Optional[str] = None, 
                 repo_owner: str = "cs320f25",
                 issues_repo: str = "hw9-issues",
                 project_repo: Optional[str] = None):
        """
        Initialize GitHub monitor
        
        Args:
            github_token: GitHub personal access token (can also use GITHUB_TOKEN env var)
            repo_owner: Owner of the repositories (default: cs320f25)
            issues_repo: Name of the issues repository to monitor
            project_repo: Name of your project repository to analyze
        """
        self.token = github_token or os.getenv('GITHUB_TOKEN')
        self.repo_owner = repo_owner
        self.issues_repo = issues_repo
        self.project_repo = project_repo
        
        self.api_base = "https://api.github.com"
        self.headers = {
            'Accept': 'application/vnd.github.v3+json'
        }
        
        if self.token:
            self.headers['Authorization'] = f'token {self.token}'
    
    def fetch_open_issues(self) -> List[Dict]:
        """
        Fetch all open issues from the hw9-issues repository
        
        Returns:
            List of issue dictionaries
        """
        url = f"{self.api_base}/repos/{self.repo_owner}/{self.issues_repo}/issues"
        params = {'state': 'open', 'per_page': 100}
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching issues: {e}")
            return []
    
    def is_mentioned(self, issue: Dict) -> bool:
        """
        Check if EIDOLON-7 is mentioned in an issue
        
        Args:
            issue: Issue dictionary from GitHub API
        
        Returns:
            True if EIDOLON-7 is mentioned (case-insensitive, semantic)
        """
        # Check title and body
        title = issue.get('title', '').lower()
        body = issue.get('body', '').lower()
        
        # List of valid mentions
        mentions = [
            'eidolon-7',
            'eidolon 7',
            'eidolon7',
            '@eidolon-7',
            'eidolon',
        ]
        
        # Check if any mention appears in title or body
        text = f"{title} {body}"
        return any(mention in text for mention in mentions)
    
    def has_responded(self, issue: Dict) -> bool:
        """
        Check if EIDOLON-7 has already responded to this issue
        
        Args:
            issue: Issue dictionary from GitHub API
        
        Returns:
            True if already responded
        """
        issue_number = issue['number']
        url = f"{self.api_base}/repos/{self.repo_owner}/{self.issues_repo}/issues/{issue_number}/comments"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            comments = response.json()
            
            # Check if any comment is from our bot or contains EIDOLON-7 signature
            for comment in comments:
                body = comment.get('body', '')
                if '⚡ EIDOLON-7' in body or 'EIDOLON-7 RESPONSE' in body:
                    return True
            
            return False
        except requests.exceptions.RequestException as e:
            print(f"Error checking comments: {e}")
            return False
    
    def post_comment(self, issue_number: int, comment_body: str) -> bool:
        """
        Post a comment to an issue
        
        Args:
            issue_number: The issue number
            comment_body: The comment text to post
        
        Returns:
            True if successful
        """
        if not self.token:
            print("Error: GitHub token required to post comments")
            print("Set GITHUB_TOKEN environment variable or pass token to constructor")
            return False
        
        url = f"{self.api_base}/repos/{self.repo_owner}/{self.issues_repo}/issues/{issue_number}/comments"
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json={'body': comment_body}
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error posting comment: {e}")
            return False
    
    def analyze_project_status(self) -> Dict:
        """
        Analyze the status of the project repository
        
        Returns:
            Dictionary with project status information
        """
        if not self.project_repo:
            return {
                'error': 'Project repository not configured'
            }
        
        # Fetch repository information
        repo_url = f"{self.api_base}/repos/{self.repo_owner}/{self.project_repo}"
        
        try:
            response = requests.get(repo_url, headers=self.headers)
            response.raise_for_status()
            repo_data = response.json()
            
            # Fetch recent commits
            commits_url = f"{repo_url}/commits"
            commits_response = requests.get(commits_url, headers=self.headers, params={'per_page': 5})
            commits_response.raise_for_status()
            recent_commits = commits_response.json()
            
            # Fetch open issues in project repo
            issues_url = f"{repo_url}/issues"
            issues_response = requests.get(issues_url, headers=self.headers, params={'state': 'open'})
            issues_response.raise_for_status()
            open_issues = issues_response.json()
            
            return {
                'name': repo_data.get('name'),
                'description': repo_data.get('description'),
                'updated_at': repo_data.get('updated_at'),
                'open_issues_count': len(open_issues),
                'recent_commits': [
                    {
                        'message': c['commit']['message'],
                        'author': c['commit']['author']['name'],
                        'date': c['commit']['author']['date']
                    }
                    for c in recent_commits
                ],
                'open_issues': [
                    {
                        'title': i['title'],
                        'number': i['number'],
                        'created_at': i['created_at']
                    }
                    for i in open_issues
                ]
            }
        except requests.exceptions.RequestException as e:
            return {
                'error': f'Failed to analyze project: {e}'
            }
    
    def generate_status_update(self, project_status: Optional[Dict] = None) -> str:
        """
        Generate a status update for the project
        
        Args:
            project_status: Optional pre-fetched project status
        
        Returns:
            Formatted status update text
        """
        if project_status is None:
            project_status = self.analyze_project_status()
        
        if 'error' in project_status:
            return f"⚡ EIDOLON-7 STATUS REPORT ⚡\n\nError: {project_status['error']}"
        
        # Build status report
        report = []
        report.append("⚡ EIDOLON-7 STATUS REPORT ⚡")
        report.append("=" * 60)
        report.append(f"Project: {project_status.get('name', 'Unknown')}")
        report.append(f"Last Updated: {project_status.get('updated_at', 'Unknown')}")
        report.append("")
        
        # Implementation status
        report.append("IMPLEMENTATION STATUS:")
        report.append("✅ Phase 1: Complete")
        report.append("  - Procedural dungeon generation (rooms + corridors)")
        report.append("  - Biome-specific enemy and resource placement")
        report.append("  - AI pathfinding validation (BFS)")
        report.append("  - ASCII visualization with overlays")
        report.append("  - Real-time animation feature")
        report.append("")
        report.append("🔧 Phase 2: In Progress")
        report.append("  - Dungeon Quality Score (DQS) system")
        report.append("  - EIDOLON-7 ADK agent (knowledge + generation services)")
        report.append("  - GitHub issue monitoring integration")
        report.append("")
        
        # Recent activity
        if project_status.get('recent_commits'):
            report.append("RECENT ACTIVITY:")
            for commit in project_status['recent_commits'][:3]:
                report.append(f"  - {commit['message']} ({commit['date'][:10]})")
            report.append("")
        
        # Open issues
        if project_status.get('open_issues_count', 0) > 0:
            report.append(f"BLOCKERS/ISSUES: {project_status['open_issues_count']} open")
            for issue in project_status.get('open_issues', [])[:3]:
                report.append(f"  - #{issue['number']}: {issue['title']}")
            report.append("")
        else:
            report.append("BLOCKERS/ISSUES: None")
            report.append("")
        
        # Next steps
        report.append("NEXT STEPS:")
        report.append("  1. Complete ADK service implementations")
        report.append("  2. Test GitHub issue monitoring")
        report.append("  3. Generate example outputs with DQS metrics")
        report.append("  4. Update documentation with ADK examples")
        report.append("")
        
        report.append("=" * 60)
        report.append("Status generated by EIDOLON-7 | Ancient Dungeon Overseer")
        
        return "\n".join(report)
    
    def check_and_respond(self) -> List[Dict]:
        """
        Main service loop: Check for mentions and respond if needed
        
        Returns:
            List of issues that were responded to
        """
        issues = self.fetch_open_issues()
        responded_to = []
        
        for issue in issues:
            # Check if EIDOLON-7 is mentioned
            if not self.is_mentioned(issue):
                continue
            
            # Check if already responded
            if self.has_responded(issue):
                continue
            
            # Generate status update
            status_update = self.generate_status_update()
            
            # Post comment
            success = self.post_comment(issue['number'], status_update)
            
            if success:
                responded_to.append({
                    'issue_number': issue['number'],
                    'title': issue['title'],
                    'url': issue['html_url']
                })
        
        return responded_to


def main():
    """
    Example usage / testing function
    """
    # Initialize monitor
    monitor = GitHubIssueMonitor(
        repo_owner="cs320f25",
        issues_repo="hw9-issues",
        project_repo="hw9-yourusername"  # Replace with actual repo
    )
    
    print("🔍 Checking for EIDOLON-7 mentions...")
    
    # Check and respond to issues
    responded = monitor.check_and_respond()
    
    if responded:
        print(f"\n✅ Responded to {len(responded)} issue(s):")
        for item in responded:
            print(f"  - Issue #{item['issue_number']}: {item['title']}")
            print(f"    {item['url']}")
    else:
        print("\n✓ No new mentions found or all already responded to")


if __name__ == '__main__':
    main()
