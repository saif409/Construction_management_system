from django.urls import path
from.import views
urlpatterns = [
    path('add/', views.supply_add, name="Add" ),
    path('list/', views.supply_list, name="list"),
    path('details/<int:id>/', views.supply_view, name="details"),
    path('update/<int:id>/', views.supply_update, name="update"),
    path('remove/<int:id>/', views.supply_remove, name="supply_remove"),
    path('add-supplier/', views.add_supplier, name="add_supplier"),
    path('update-supplier/<int:id>/', views.update_supplier, name="update_supplier"),
    path('remove-supplier/<int:id>/', views.remove_supplier, name="remove_supplier"),
    # path('stock/list/', views.stock_list, name="stock_list"),
    # path('site-manager-request', views.site_manager_request, name="site_manager_request"),
    # path('site-manager-request-list/<str:filter>/', views.site_manager_request_list, name="site_manager_request_list"),
    # path('site-manager-request-list/<str:filter>/', views.site_manager_request_list, name="site_manager_request_list"),
    # path('add-new-stock/', views.add_new_stock, name="add_new_stock"),
    # path('site-manager-request-delete/<int:id>/', views.site_manager_request_delete, name="site_manager_request_delete")
    #

]