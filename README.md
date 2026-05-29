# Agent Production Status Dashboard

A simple, shared project status dashboard hosted on GitHub Pages.

## Structure

- `index.html` — The visual dashboard (loads data dynamically)
- `projects.json` — Contains all project data (this is the file you edit)

## How to Update Project Status

1. Edit `projects.json`
2. Update the relevant fields for a project:
   - `status`: "Active", "Exploration", "New", "Paused", or "Completed"
   - `phase`: Current stage of the project
   - `last_updated`: Use YYYY-MM-DD format
   - `notes`: Any relevant notes
3. Commit and push the changes

```bash
git add projects.json
git commit -m "Update project status"
git push
```

The dashboard will automatically reflect the changes within a minute or two.

## Adding a New Project

Add a new object to the `projects.json` array with the following structure:

```json
{
  "id": "unique-project-id",
  "name": "Project Name",
  "description": "Short description",
  "status": "Active",
  "phase": "Current Phase",
  "last_updated": "2026-01-28",
  "notes": "Optional notes",
  "thread_id": null
}
```

## Future Automation

The agent can update this dashboard by modifying `projects.json`.  
A future workflow could allow the agent to automatically commit and push updates when project status changes in Discord threads.

## Live Dashboard

https://happydestiny79.github.io/agent-production-status/
