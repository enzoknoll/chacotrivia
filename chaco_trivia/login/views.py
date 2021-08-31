from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from os import getcwd
import pyodbc
import random


# for pregunta in cursor.execute('SELECT preguntas, respuesta1, respuesta2, respuesta3, respuesta4 FROM Preguntas WHERE id=(Int(5 * Rnd) +1)'):
#     print(pregunta)


# def home(request):
#     conn = pyodbc.connect(
#         "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/Droshi/Desktop/Django final/venvtriviachaco/chaco_trivia/login/templates/preguntassql/preguntas.accdb;")
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM Preguntas')

#     # numx=random.randint(1,5)
#     # preguntas=cursor.fetchmany(numx)
#     for pregunta in cursor.execute('SELECT preguntas, respuesta1, respuesta2, respuesta3, respuesta4, ans, categoria FROM Preguntas WHERE id=(Int(5 * Rnd) +1)'):
#         print(pregunta)
#     listapr = pregunta
#     if request.method == 'POST':
#         print(request.POST)
#         # questions = QuesModel.objects.all()

#         score = 0
#         wrong = 0
#         correct = 0
#         total = 0
#         for ans in listapr:
#             total += 1
#             print(request.POST.get(listapr[24]))
#             print(listapr[123])
#             if listapr[12] == request.POST.get(listapr[55]):
#                 score += 10
#                 correct += 1
#             else:
#                 wrong += 1
#         context = {
#             'score': score,
#             'time': request.POST.get('timer'),
#             'correct': correct,
#             'wrong': wrong,
#             # 'percent': percent,
#             'total': total
#         }
#         return render(request, 'quiz/result.html', context)
#     else:
#         pregunta = listapr[0]
#         respuesta1 = listapr[1]
#         respuesta2 = listapr[2]
#         respuesta3 = listapr[3]
#         respuesta4 = listapr[4]
#         questions = QuesModel.objects.all()
#         context = {
#             'questions': questions,
#             'pregunta': pregunta,
#             'respuesta1': respuesta1,
#             'respuesta2': respuesta2,
#             'respuesta3': respuesta3,
#             'respuesta4': respuesta4
#         }
#         return render(request, 'quiz/Homealeatorio.html', context)

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.all()
        context = {
            'questions': questions,
        }
        return render(request, 'quiz/Home.html', context)

def homehistoria(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.filter(
            categoria = 3
        )
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.filter(
            categoria = 3
        )
        context = {
            'questions': questions,
        }
        return render(request, 'quiz/Home.html', context)

def homedeportes(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.filter(
            categoria = 4
        )
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.filter(
            categoria = 4
        )
        context = {
            'questions': questions,
        }
        return render(request, 'quiz/Home.html', context)

def homegastronomia(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.filter(
            categoria = 5
        )
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.filter(
            categoria = 5
        )
        context = {
            'questions': questions,
        }
        return render(request, 'quiz/Home.html', context)

def homecienciasnaturales(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.filter(
            categoria = 6
        )
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.filter(
            categoria = 6
        )
        context = {
            'questions': questions,
        }
        return render(request, 'quiz/Home.html', context)

def homegeografia(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.filter(
            categoria = 7
        )
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.filter(
            categoria = 7
        )
        context = {
            'questions': questions,
        }
        return render(request, 'quiz/Home.html', context)

def homepolitica(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.filter(
            categoria = 8
        )
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.filter(
            categoria = 8
        )
        context = {
            'questions': questions,
        }
        return render(request, 'quiz/Home.html', context)


def lobby(request):
    return render(request, 'lobby/index.html')


def addQuestion(request):
    if request.user.is_staff:
        form = addQuestionform()
        if(request.method == 'POST'):
            form = addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'quiz/addQuestion.html', context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'quiz/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/lobby')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/lobby')
        context = {}
        return render(request, 'quiz/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
