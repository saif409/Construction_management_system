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

    path('labour_type/', views.labour_type, name="labour_type"),
    path('update-labour-type/<int:id>/', views.update_labour_type, name="update_labour_type"),
    path('remove_labour_type/<int:id>/', views.remove_labour_type, name="remove_labour_type"),

    path('labour_list/', views.labour_list, name="labour_list"),
    path('add-new-labour/', views.add_new_labour, name="add_new_labour"),
    path('remove_labour/<int:id>/', views.remove_labour, name="remove_labour"),
    path('labour_update/<int:id>/', views.labour_update, name="labour_update"),

    path('add-labour-work-time/', views.add_labour_work_time, name="add_labour_work_time"),
    path('update-labour-work-time/<int:id>/', views.update_labour_work_time, name="update_labour_work_time"),
    path('work-time-list/', views.work_time_list, name="work_time_list"),
    path('remove-work-list/<int:id>/', views.remove_work_list, name="remove_work_list"),


    path('stock-list/', views.stock_list, name="stock_list"),
    path('remove-stock/<int:id>/', views.remove_stock, name="remove_stock"),
    path('add-new-stock/', views.add_new_stock, name="add_new_stock"),
    path('update-stock/<int:id>/', views.update_stock, name="update_stock"),

    path('stock-management/', views.stock_management, name="stock_management"),
    path('remove-stock-management/<int:id>/', views.remove_stock_management, name="remove_stock_management"),
    path('add/stock/management/', views.add_stock_management, name="add_stock_management"),
    path('update-stock-management/<int:id>/', views.update_stock_management, name="update_stock_management"),

    path('add-new-client', views.add_new_client, name="add_new_client"),
    path('update-client/<int:id>/', views.update_client, name="update_client"),
    path('remove-client/<int:id>/', views.remove_client, name="remove_client"),
    path('client-list/', views.client_list, name="client_list"),


    # path('site-manager-request', views.site_manager_request, name="site_manager_request"),
    # path('site-manager-request-list/<str:filter>/', views.site_manager_request_list, name="site_manager_request_list"),
    # path('site-manager-request-list/<str:filter>/', views.site_manager_request_list, name="site_manager_request_list"),
    # path('site-manager-request-delete/<int:id>/', views.site_manager_request_delete, name="site_manager_request_delete")
    #

]