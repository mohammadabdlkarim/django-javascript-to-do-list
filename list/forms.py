from django import forms

class CreateListForm(forms.Form):
    list_name = forms.CharField(max_length=50, required=True, label="List Name")


class AddTaskForm(forms.Form):
    task_content = forms.CharField(max_length=1000, required=True, label="Task Content")
    done = forms.BooleanField(required=False)