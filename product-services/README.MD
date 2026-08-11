written code follow

1-> start with models
   Category Model
   product model
   Product Image model
   Product Variant Model

2 -> Schemas
    Category Schema
    Product Schema
    product Image Schema
    Product Variants Schema

3 -> Repository
    Category Repository
        create_category()
        get_category_by_id()
        get_category_by_name()
        get_category_by_slug()
        get_all_categories()
        update_category()
        delete_category()

    product Repository
        create_product()
        get_product_by_id()
        get_product_by_slug()
        get_all_products()
        update_product()
        delete_product()

    Product Variant Repository
        create_variant()
        get_variant_by_id()
        get_variants_by_product_id()
        update_variant()
        delete_variant()
    
    Product Image Repository
        add_image()
        get_images_by_product_id()
        delete_image()


4 -> Services
    category_service
        create_category_service()
        get_category_by_id_service()
        get_all_categories_router()
        get_category_by_name_service()
        get_category_by_slug_name()
        update_category_service()
        delete_category_service()

    Product_service
        create_product_service()
        get_all_products_service()
        get_product_by_id_service()
        get_product_by_name_service()
        get_product_by_slug_service()
        update_product_service()
        delete_product_service()



5 -> Router
    category_router
        create_category_router()
        get_category_by_id_router()
        get_all_categories_router()
        get_category_by_name_router()
        get_category_by_slug_router()
        update_category_router()
        delete_category_router()

