from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserGroup(models.Model):
	user = models.OneToOneField(User, related_name="group")
	group = models.CharField(max_length=128, null=True)
	
	def __str__(self):
		return self.group

class Lesson(models.Model):
	name = models.CharField(max_length=512, null=True)
	teacher = models.CharField(max_length=512, null=True)
	room = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.name

class Day(models.Model):
	para1 = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
	para2 = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="a1", null=True, blank=True)
	para3 = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="a2", null=True, blank=True)
	para4 = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="a3", null=True, blank=True)
	para5 = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="a4", null=True, blank=True)
	group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=True, blank=True)
	date = models.PositiveIntegerField(null=True)

	def __str__(self):
		return str(self.date)