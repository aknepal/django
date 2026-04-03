from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Manager, Player
from .forms import TeamForm, ManagerForm, PlayerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def logout_page(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_page')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# ---------------- PAGE 1 ----------------
@login_required
@login_required
def admin_page(request):
    teams = Team.objects.all()

    team_form = TeamForm()
    manager_form = ManagerForm()
    player_form = PlayerForm()

    if request.method == "POST":

        # ---------------- TEAM ----------------
        if "team_add" in request.POST:
            form = TeamForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_page')

        if "team_edit" in request.POST:
            team = Team.objects.get(id=request.POST['id'])
            form = TeamForm(request.POST, instance=team)
            if form.is_valid():
                form.save()
                return redirect('admin_page')

        if "team_delete" in request.POST:
            Team.objects.get(id=request.POST['id']).delete()
            return redirect('admin_page')

        # ---------------- MANAGER ----------------
        if "manager_add" in request.POST:
            team_id = request.POST.get('team')
    
            manager, created = Manager.objects.get_or_create(
                 team_id=team_id
        )

            form = ManagerForm(request.POST, request.FILES, instance=manager)
            if form.is_valid():
                 form.save()
    
            return redirect('admin_page')

        # ---------------- PLAYER ----------------
        if "player_add" in request.POST:
            form = PlayerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_page')

    return render(request, "admin.html", {
        "teams": teams,
        "team_form": team_form,
        "manager_form": manager_form,
        "player_form": player_form
    })
def league_table(request):
    teams = Team.objects.all().order_by('-win', '-goal_difference')
    return render(request, "league.html", {"teams": teams})

def team_detail(request, pk):
    team = get_object_or_404(Team, id=pk)
    manager = Manager.objects.filter(team=team).first()
    players = Player.objects.filter(team=team)

    return render(request, "detail.html", {
        "team": team,
        "manager": manager,
        "players": players
    })