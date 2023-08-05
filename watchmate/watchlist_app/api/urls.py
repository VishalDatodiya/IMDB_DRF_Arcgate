from django.urls import path

# from watchlist_app.api.views import watchlist, watchlistDetail
from watchlist_app.api.views import WatchlistAV, WatchlistDetail, PlatformList, StreamDetail, ReviewList, ReviewDetail, CreateReview

urlpatterns = [
    path('list/', WatchlistAV.as_view(), name="list"),
    path('list/<int:pk>/', WatchlistDetail.as_view(), name="detail"),
    path('stream/', PlatformList.as_view(), name="stream"),
    path('stream/<int:pk>/', StreamDetail.as_view(), name="stream-detail"),
    # path('reviews/', ReviewList.as_view(), name="reviews"),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
    
    path('<int:pk>/create-review/', CreateReview.as_view(), name="create-review"),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="reviews"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
]
