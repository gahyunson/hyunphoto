from django.shortcuts import render

def main(request):
    try:
        print('Start Test')
        raise BaseException
    except BaseException as e:
        print('BaseException')
    else:
        print('Non-Exception')
    finally:
        print('Done Test')
    return render(request, 'main.html')