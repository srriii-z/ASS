from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def browse(request):
    games = [
        {'title': 'Game 1', 'genre': 'Action', 'image': 'assets/images/game-01.jpg'},
        {'title': 'Game 2', 'genre': 'RPG', 'image': 'assets/images/game-02.jpg'},
        {'title': 'Game 3', 'genre': 'Adventure', 'image': 'assets/images/game-03.jpg'},
    ]
    context = {'games': games}
    return render(request, 'browse.html', context)



def details(request):
    return render(request, 'details.html')


def streams(request):
    # If your streams.html needs context, you can pass data here.
    # Currently, your streams.html just loops over hardcoded numbers ('1234', etc.)
    # But here’s a better example if you want to send data:
    streams_list = [
        {'title': 'Game 1', 'viewers': '2.4K', 'downloads': '249K', 'rating': '4.8', 'image': 'assets/images/featured-01.jpg'},
        {'title': 'Game 2', 'viewers': '1.8K', 'downloads': '150K', 'rating': '4.6', 'image': 'assets/images/featured-02.jpg'},
        # more streams if needed…
    ]
    top_streamers = [
        {'name': 'Streamer 1', 'avatar': 'assets/images/avatar-01.jpg'},
        {'name': 'Streamer 2', 'avatar': 'assets/images/avatar-02.jpg'},
        # …
    ]
    context = {
        'streams_list': streams_list,
        'top_streamers': top_streamers,
    }
    return render(request, 'streams.html', context)


def profile(request):
    clips = [
        {'image': 'assets/images/clip-01.jpg', 'link': 'https://youtube.com/watch?v=clip1', 'title': 'Clip 1', 'views': 300},
        {'image': 'assets/images/clip-02.jpg', 'link': 'https://youtube.com/watch?v=clip2', 'title': 'Clip 2', 'views': 280},
        {'image': 'assets/images/clip-03.jpg', 'link': 'https://youtube.com/watch?v=clip3', 'title': 'Clip 3', 'views': 260},
        {'image': 'assets/images/clip-04.jpg', 'link': 'https://youtube.com/watch?v=clip4', 'title': 'Clip 4', 'views': 240},
    ]

    games = [
        {'image': 'assets/images/game-01.jpg', 'title': 'Game 1', 'genre': 'Action', 'date_added': '2025-01-01', 'hours_played': '25', 'status': 'Downloaded'},
        {'image': 'assets/images/game-02.jpg', 'title': 'Game 2', 'genre': 'Adventure', 'date_added': '2025-02-15', 'hours_played': '12', 'status': 'Downloaded'},
        {'image': 'assets/images/game-03.jpg', 'title': 'Game 3', 'genre': 'RPG', 'date_added': '2025-03-20', 'hours_played': '40', 'status': 'Downloaded'},
    ]

    stats = {
        'games_downloaded': len(games),
        'friends_online': 16,
        'live_streams': 0,
        'clips': len(clips),
    }

    context = {
        'user_name': 'Alan Smithee',
        'clips': clips,
        'games': games,
        'stats': stats,
    }

    return render(request, 'profile.html', context)
