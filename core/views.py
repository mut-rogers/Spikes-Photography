from django.shortcuts import render
from django.views import View


class HomepageView(View):

    def get(self, request):
        return render(self.request, "homepage.html")
