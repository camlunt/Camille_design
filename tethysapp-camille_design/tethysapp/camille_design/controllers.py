from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {}

    return render(request, 'camille_design/home.html', context)


@login_required()
def proposal(request):
    """
    Controller for the app project proposal page.
    """

    context = {}

    return render(request, 'camille_design/proposal.html', context)

@login_required()
def wireframes(request):
    """
    Controller for the app wireframe mockups page.
    """

    context = {}

    return render(request, 'camille_design/wireframes.html', context)