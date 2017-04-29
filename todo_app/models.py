from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=1000)
    priority = models.SmallIntegerField()
    done = models.BooleanField()
    project = models.ForeignKey(Project)

    def __str__(self):
        return "[{},{}]{}".format(self.priority, "Done" if self.done else "Not done", self.text)


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
