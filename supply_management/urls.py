from django.urls import path
from.import views
urlpatterns = [
    path('add/', views.supply_add, name="Add" ),
    path('list/', views.supply_list, name="list"),
    path('details/<int:id>/', views.supply_view, name="details"),
    path('update/<int:id>/', views.supply_update, name="update"),
    path('remove/<int:id>/', views.supply_remove, name="supply_remove"),

    path('add-supplier/', views.add_supplier, name="add_supplier"),
    path('supplier-list/', views.supplier_list, name="supplier_list"),
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

    path('add-labour-request/', views.add_labour_request, name="add_labour_request"),
    path('labour-request-list/<str:filter>/', views.labour_request_list, name="labour_request_list"),
    path('update-labour-request/<int:id>/', views.update_labour_request, name="update_labour_request"),
    path('remove-labour-request/<int:id>/', views.remove_labour_request, name="remove_labour_request"),

    path('stock-list/', views.stock_list, name="stock_list"),
    path('remove-stock/<int:id>/', views.remove_stock, name="remove_stock"),
    path('add-new-stock/', views.add_new_stock, name="add_new_stock"),
    path('update-stock/<int:id>/', views.update_stock, name="update_stock"),

    path('stock-management/', views.stock_management, name="stock_management"),
    path('remove-stock-management/<int:id>/', views.remove_stock_management, name="remove_stock_management"),
    path('add/stock/management/', views.add_stock_management, name="add_stock_management"),
    path('update-stock-management/<int:id>/', views.update_stock_management, name="update_stock_management"),

    path('add-new-client/', views.add_new_client, name="add_new_client"),
    path('update-client/<int:id>/', views.update_client, name="update_client"),
    path('remove-client/<int:id>/', views.remove_client, name="remove_client"),
    path('client-list/', views.client_list, name="client_list"),


    path('register-surveyor/', views.register_surveyor, name="register_surveyor"),
    path('surveyor-list/<str:filter>/', views.surveyor_list, name="surveyor_list"),
    path('surveyor-details/<int:id>/', views.view_surveyor, name="view_surveyor"),
    path('update-surveyor/<int:id>/', views.update_surveyor, name="update_surveyor"),
    path('remove-surveyor/<int:id>/', views.remove_surveyor, name="remove_surveyor"),

    path('site-manager-request', views.site_manager_request, name="site_manager_request"),
    path('site-manager-request-list/<str:filter>/', views.site_manager_request_list, name="site_manager_request_list"),
    path('site-manager-request-delete/<int:id>/', views.site_manager_request_delete, name="site_manager_request_delete"),
    path('site-manager-update/<int:id>/', views.site_manager_update, name="site_manager_update"),


    path('cost_estimation/<int:id>/', views.cost_estimation_details, name="cost_estimation"),
    path('cost_estimation_pdf/', views.cost_estimation_pdf_view, name='cost_pdf_view'),
    #path('cost_estimation_pdf_download/', views.cost_estimation_pdf_download.as_view(), name='cost_pdf_download'),
    path('estimate/', views.estimate, name='estimate'),


    path('material_list/', views.material, name='material_list'),
    path('material_remove/<int:id>/', views.material_remove, name='material_remove'),


    path('cement-price/', views.cement_price, name='cement_price'),
    path('steel-price/', views.steel_price, name='steel_price'),
    path('aggregate-price/', views.aggregate_price, name='aggregate_price'),
    path('bricks-price/', views.bricks_price, name='bricks_price'),
    path('electric-fitting-price/', views.electric_fitting_price, name='electric_fitting_price'),
    path('flooring-price/', views.flooring_price, name='flooring_price'),
    path('painting-price/', views.painting_price, name='painting_price'),
    path('sand-price/', views.sand_price, name='sand_price'),
    path('sanitary-price/', views.sanitary_price, name='sanitary_price'),
    path('labour-price/', views.add_labour_price, name='add_labour_price'),


    path('construction-site-list/', views.construction_site_list, name='construction_list'),
    path('add-new-construction-site/', views.add_new_construction_site, name='add_new_construction_site'),
    path('remove-contruction-site/<int:id>/', views.remove_contruction_site, name='remove_contruction_site'),
    path('update-construction-site/<int:id>/', views.update_construction_site, name='update_construction_site'),

    path('stock_request_to_supplier/', views.stock_request_to_supplier, name="stock_request_to_supplier"),
    path('stock_manager_request_list_update/<int:id>/', views.stock_manager_request_list_update, name="stock_manager_request_list_update"),
    path('stock_manager_request_list_remove/<int:id>/', views.stock_manager_request_list_remove, name="stock_manager_request_list_remove"),
    path('stock-manager-request-list/<str:filter>/', views.stock_manager_request_list, name='stock_manager_request_list'),


    path('notification-list/', views.notification_list, name='notification_list'),
    path('remove-notification/<int:id>/', views.remove_notification, name='remove_notification'),


    path('invoice_list', views.invoice_list, name='invoice_list'),
    path('add_new_invoice', views.add_new_invoice, name='add_new_invoice'),
    path('invoice_details/<int:id>/', views.invoice_details, name='invoice_details'),
    path('invoice_remove<int:id>/', views.invoice_remove, name='invoice_remove'),

    path('request_stock', views.request_stock, name='request_stock'),
    path('add_new_request_stock', views.add_new_request_stock, name='add_new_request_stock'),


    path('report-generation/<str:filter>/', views.report_generation, name='report_generation'),




]