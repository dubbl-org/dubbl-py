from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._base_client import AsyncAPIClient, SyncAPIClient


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


class Projects:
    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(self, **params: Any) -> Any:
        return self._client.get("/projects", params={k: v for k, v in params.items() if v is not None})

    def create(self, **kwargs: Any) -> Any:
        return self._client.post("/projects", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def retrieve(self, id: str) -> Any:
        return self._client.get(f"/projects/{id}")

    def update(self, id: str, **kwargs: Any) -> Any:
        return self._client.patch(f"/projects/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    def delete(self, id: str) -> Any:
        return self._client.delete(f"/projects/{id}")

    # Labels
    def list_labels(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/labels")

    def create_label(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/labels", json=body)

    # Members
    def list_members(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/members")

    def add_member(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/members", json=body)

    def remove_member(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.delete(f"/projects/{project_id}/members", json=body)

    # Teams
    def list_teams(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/teams")

    def create_team(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/teams", json=body)

    def list_team_assignments(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/team-assignments")

    def create_team_assignment(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/team-assignments", json=body)

    def delete_team_assignment(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.delete(f"/projects/{project_id}/team-assignments", json=body)

    # Milestones
    def list_milestones(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/milestones")

    def create_milestone(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/milestones", json=body)

    def retrieve_milestone(self, project_id: str, milestone_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/milestones/{milestone_id}")

    def update_milestone(self, project_id: str, milestone_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/projects/{project_id}/milestones/{milestone_id}", json=body)

    def delete_milestone(self, project_id: str, milestone_id: str) -> Any:
        return self._client.delete(f"/projects/{project_id}/milestones/{milestone_id}")

    def list_milestone_assignments(self, project_id: str, milestone_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/milestones/{milestone_id}/assignments")

    def create_milestone_assignment(self, project_id: str, milestone_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/milestones/{milestone_id}/assignments", json=body)

    def update_milestone_assignments(self, project_id: str, milestone_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/projects/{project_id}/milestones/{milestone_id}/assignments", json=body)

    # Tasks
    def list_tasks(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/tasks")

    def create_task(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/tasks", json=body)

    def retrieve_task(self, project_id: str, task_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/tasks/{task_id}")

    def update_task(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/projects/{project_id}/tasks/{task_id}", json=body)

    def delete_task(self, project_id: str, task_id: str) -> Any:
        return self._client.delete(f"/projects/{project_id}/tasks/{task_id}")

    def get_task_checklist(self, project_id: str, task_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/tasks/{task_id}/checklist")

    def create_task_checklist_item(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/tasks/{task_id}/checklist", json=body)

    def update_task_checklist(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/projects/{project_id}/tasks/{task_id}/checklist", json=body)

    def delete_task_checklist_item(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.delete(f"/projects/{project_id}/tasks/{task_id}/checklist", json=body)

    # Task comments
    def list_task_comments(self, project_id: str, task_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/tasks/{task_id}/comments")

    def create_task_comment(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/tasks/{task_id}/comments", json=body)

    # Notes
    def list_notes(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/notes")

    def create_note(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/notes", json=body)

    # Time entries
    def list_time_entries(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/time-entries")

    def create_time_entry(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/time-entries", json=body)

    def retrieve_time_entry(self, project_id: str, entry_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/time-entries/{entry_id}")

    def update_time_entry(self, project_id: str, entry_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.patch(f"/projects/{project_id}/time-entries/{entry_id}", json=body)

    def delete_time_entry(self, project_id: str, entry_id: str) -> Any:
        return self._client.delete(f"/projects/{project_id}/time-entries/{entry_id}")

    # Timer
    def get_timer(self, project_id: str) -> Any:
        return self._client.get(f"/projects/{project_id}/timer")

    def toggle_timer(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/timer", json=body)

    # Invoicing
    def create_invoice(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/invoice", json=body)

    def create_progress_invoice(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return self._client.post(f"/projects/{project_id}/progress-invoice", json=body)


class AsyncProjects:
    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(self, **params: Any) -> Any:
        return await self._client.get("/projects", params={k: v for k, v in params.items() if v is not None})

    async def create(self, **kwargs: Any) -> Any:
        return await self._client.post("/projects", json={_to_camel(k): v for k, v in kwargs.items() if v is not None})

    async def retrieve(self, id: str) -> Any:
        return await self._client.get(f"/projects/{id}")

    async def update(self, id: str, **kwargs: Any) -> Any:
        return await self._client.patch(
            f"/projects/{id}", json={_to_camel(k): v for k, v in kwargs.items() if v is not None}
        )

    async def delete(self, id: str) -> Any:
        return await self._client.delete(f"/projects/{id}")

    # Labels
    async def list_labels(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/labels")

    async def create_label(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/labels", json=body)

    # Members
    async def list_members(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/members")

    async def add_member(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/members", json=body)

    async def remove_member(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.delete(f"/projects/{project_id}/members", json=body)

    # Teams
    async def list_teams(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/teams")

    async def create_team(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/teams", json=body)

    async def list_team_assignments(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/team-assignments")

    async def create_team_assignment(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/team-assignments", json=body)

    async def delete_team_assignment(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.delete(f"/projects/{project_id}/team-assignments", json=body)

    # Milestones
    async def list_milestones(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/milestones")

    async def create_milestone(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/milestones", json=body)

    async def retrieve_milestone(self, project_id: str, milestone_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/milestones/{milestone_id}")

    async def update_milestone(self, project_id: str, milestone_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/projects/{project_id}/milestones/{milestone_id}", json=body)

    async def delete_milestone(self, project_id: str, milestone_id: str) -> Any:
        return await self._client.delete(f"/projects/{project_id}/milestones/{milestone_id}")

    async def list_milestone_assignments(self, project_id: str, milestone_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/milestones/{milestone_id}/assignments")

    async def create_milestone_assignment(self, project_id: str, milestone_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/milestones/{milestone_id}/assignments", json=body)

    async def update_milestone_assignments(self, project_id: str, milestone_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/projects/{project_id}/milestones/{milestone_id}/assignments", json=body)

    # Tasks
    async def list_tasks(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/tasks")

    async def create_task(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/tasks", json=body)

    async def retrieve_task(self, project_id: str, task_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/tasks/{task_id}")

    async def update_task(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/projects/{project_id}/tasks/{task_id}", json=body)

    async def delete_task(self, project_id: str, task_id: str) -> Any:
        return await self._client.delete(f"/projects/{project_id}/tasks/{task_id}")

    async def get_task_checklist(self, project_id: str, task_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/tasks/{task_id}/checklist")

    async def create_task_checklist_item(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/tasks/{task_id}/checklist", json=body)

    async def update_task_checklist(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/projects/{project_id}/tasks/{task_id}/checklist", json=body)

    async def delete_task_checklist_item(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.delete(f"/projects/{project_id}/tasks/{task_id}/checklist", json=body)

    # Task comments
    async def list_task_comments(self, project_id: str, task_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/tasks/{task_id}/comments")

    async def create_task_comment(self, project_id: str, task_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/tasks/{task_id}/comments", json=body)

    # Notes
    async def list_notes(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/notes")

    async def create_note(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/notes", json=body)

    # Time entries
    async def list_time_entries(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/time-entries")

    async def create_time_entry(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/time-entries", json=body)

    async def retrieve_time_entry(self, project_id: str, entry_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/time-entries/{entry_id}")

    async def update_time_entry(self, project_id: str, entry_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.patch(f"/projects/{project_id}/time-entries/{entry_id}", json=body)

    async def delete_time_entry(self, project_id: str, entry_id: str) -> Any:
        return await self._client.delete(f"/projects/{project_id}/time-entries/{entry_id}")

    # Timer
    async def get_timer(self, project_id: str) -> Any:
        return await self._client.get(f"/projects/{project_id}/timer")

    async def toggle_timer(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/timer", json=body)

    # Invoicing
    async def create_invoice(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/invoice", json=body)

    async def create_progress_invoice(self, project_id: str, **kwargs: Any) -> Any:
        body = {_to_camel(k): v for k, v in kwargs.items() if v is not None}
        return await self._client.post(f"/projects/{project_id}/progress-invoice", json=body)
