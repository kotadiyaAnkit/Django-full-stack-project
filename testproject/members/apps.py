from django.apps import AppConfig
from flask import Flask, render_template, request, redirect, url_for


class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'

