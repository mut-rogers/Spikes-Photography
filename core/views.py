from django.shortcuts import render
from django.views import View


class HomepageView(View):
    """This view renders site's home page"""

    def get(self, request):
        return render(self.request, "homepage.html")
