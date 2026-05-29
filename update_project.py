#!/usr/bin/env python3
"""
Helper script to update project status in the dashboard.

Usage examples:
    python update_project.py ufli-phonics --status "Active" --phase "Testing"
    python update_project.py genes-rehab --notes "Added payment integration"
    python update_project.py minecraft-50-states --status "Active" --phase "Design"
"""

import json
import argparse
from datetime import datetime
from pathlib import Path

PROJECTS_FILE = Path(__file__).parent / "projects.json"

def load_projects():
    with open(PROJECTS_FILE, "r") as f:
        return json.load(f)

def save_projects(projects):
    with open(PROJECTS_FILE, "w") as f:
        json.dump(projects, f, indent=2)

def update_project(project_id, status=None, phase=None, notes=None):
    projects = load_projects()
    
    for project in projects:
        if project["id"] == project_id:
            if status:
                project["status"] = status
            if phase:
                project["phase"] = phase
            if notes:
                project["notes"] = notes
            
            # Always update the last_updated date
            project["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            
            save_projects(projects)
            print(f"✅ Updated project: {project['name']}")
            return
    
    print(f"❌ Project with ID '{project_id}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update project status")
    parser.add_argument("project_id", help="Project ID (e.g. ufli-phonics)")
    parser.add_argument("--status", help="New status (Active, Exploration, New, Paused, Completed)")
    parser.add_argument("--phase", help="Current phase of the project")
    parser.add_argument("--notes", help="Notes about the project")
    
    args = parser.parse_args()
    
    update_project(args.project_id, args.status, args.phase, args.notes)