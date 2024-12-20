from django.urls import path
from .views import (
    LoginView,
    RegistrationView,
    HomePage,
    LogoutPage,
    ProfileView,
    TaskCreateView,
    TaskView,
    TaskDetails,
    CommentView,
    DeleteTask,
    TaskUpdateView,
    CommentShow,
    UserCreate,
    UserList,
    TaskSearch,
    SubTaskCreateView,
    ShowSubTasks,
    SubTaskEditView,
)

urlpatterns = [
    path("", LoginView.as_view(), name="login_form"),
    path("signup-form/", RegistrationView.as_view(), name="signup_form"),
    path("home-page/", HomePage.as_view(), name="home_page"),
    # path('userhome/',userhome.as_view(),name="userhome"),
    path("logout-page/", LogoutPage.as_view(), name="logout_page"),
    path("profile-view/", ProfileView.as_view(), name="profile_view"),
    path("task-create/", TaskCreateView.as_view(), name="task_create"),
    path("task-view/", TaskView.as_view(), name="task_view"),
    path("task-details/<int:id>", TaskDetails.as_view(), name="task_details"),
    path("delete-task/<int:id>", DeleteTask.as_view(), name="delete_task"),
    path("comment-data/<int:id>", CommentView.as_view(), name="comment_data"),
    path("comment-show/<int:id>", CommentShow.as_view(), name="comment_show"),
    path("update-task/<int:id>", TaskUpdateView.as_view(), name="update_task"),
    path("user-create/", UserCreate.as_view(), name="user_create"),
    path("user-List/", UserList.as_view(), name="user_list"),
    path("task-search/", TaskSearch.as_view(), name="task_search"),
    path(
        "taskcreate-subtask/<int:id>/",
        SubTaskCreateView.as_view(),
        name="subtask_createview",
    ),
    path("task/<int:id>/", ShowSubTasks.as_view(), name="subtask_showview"),
    path(
        "subtask/<int:id>/", SubTaskEditView.as_view(), name="subtask_editview"
    ),
]
