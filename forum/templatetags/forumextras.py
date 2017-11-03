from django import template

register = template.Library()

@register.filter
def get_total_subject_comments(subject):
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.comments.count()
    return total_posts