### BUILDING SIMPLE CRM USING DJANGO V3.2 BASED ON JUSTDJANGO TUTORIALS ON YOUTUBE


#### 1. Create project, app and mysql database

        new file:   .gitignore
        new file:   README.md
        new file:   apps/leads/__init__.py
        new file:   apps/leads/admin.py
        new file:   apps/leads/apps.py
        new file:   apps/leads/migrations/__init__.py
        new file:   apps/leads/models.py
        new file:   apps/leads/tests.py
        new file:   apps/leads/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. The project structures

        E:.
        │   .gitignore
        │   manage.py
        │   README.md
        │
        ├───apps
        │   └───leads
        │       │   admin.py
        │       │   apps.py
        │       │   models.py
        │       │   tests.py
        │       │   views.py
        │       │   __init__.py
        │       │
        │       └───migrations
        │               __init__.py
        │
        └───config
                .env
                asgi.py
                settings.py
                urls.py
                wsgi.py
                __init__.py


#### 3. Create Lead model

        modified:   README.md
        modified:   apps/leads/admin.py
        new file:   apps/leads/migrations/0001_initial.py
        modified:   apps/leads/models.py


#### 4. Create CustomUser and Agent models

        modified:   README.md
        modified:   apps/leads/admin.py
        modified:   apps/leads/migrations/0001_initial.py
        new file:   apps/leads/migrations/0002_rename_user_agent_customuser.py
        modified:   apps/leads/models.py
        modified:   config/settings.py


#### 5. Create string method 
       
       modified:   README.md
       modified:   apps/leads/models.py


#### 6. Register models to admin

        modified:   README.md
        modified:   apps/leads/admin.py


#### 7. Hellow world view 

        modified:   README.md
        modified:   apps/leads/views.py
        modified:   config/urls.py


#### 8. Templates and rendering them in the response

        modified:   README.md
        modified:   apps/leads/views.py
        modified:   config/settings.py
        new file:   templates/leads/home_page.html
        new file:   templates/second_page.html


#### 9. Context and template syntax

        modified:   README.md
        modified:   apps/leads/views.py
        modified:   templates/second_page.html


#### 10. Url namespace for leads app

        modified:   README.md
        new file:   apps/leads/urls
        modified:   config/urls.py


#### 11. Lead list and detail views
       
        modified:   README.md
        modified:   apps/leads/urls.py
        modified:   apps/leads/views.py
        new file:   templates/leads/lead_detail.html
        new file:   templates/leads/lead_list.html


#### 12. Form and lead create view

        modified:   README.md
        new file:   apps/leads/forms.py
        modified:   apps/leads/urls.py
        modified:   apps/leads/views.py
        new file:   templates/leads/lead_create.html


#### 13. Lead model form

        modified:   README.md
        modified:   apps/leads/forms.py
        modified:   apps/leads/views.py
        modified:   templates/leads/lead_detail.html
        modified:   templates/leads/lead_list.html


#### 14. Lead update view

        modified:   README.md
        modified:   apps/leads/urls.py
        modified:   apps/leads/views.py
        new file:   templates/leads/lead_update.html


#### 15. Lead delete view and Url names

        modified:   README.md
        modified:   apps/leads/urls.py
        modified:   apps/leads/views.py
        modified:   templates/leads/lead_create.html
        modified:   templates/leads/lead_detail.html
        modified:   templates/leads/lead_list.html
        modified:   templates/leads/lead_update.html


#### 16. Extended templates

        modified:   README.md
        new file:   templates/base.html
        new file:   templates/leads/base.html
        modified:   templates/leads/lead_create.html
        modified:   templates/leads/lead_detail.html
        modified:   templates/leads/lead_list.html
        modified:   templates/leads/lead_update.html
        new file:   templates/scripts.html


#### 17. Added tailwindcss

        > Install: pip install crispy-tailwind
        > Install: pip install crispy-tailwind
        > Install: pip install django-tailwind

        modified:   README.md
        modified:   apps/leads/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/base.html
        new file:   templates/landing.html
        deleted:    templates/leads/base.html
        modified:   templates/leads/lead_create.html
        modified:   templates/leads/lead_detail.html
        modified:   templates/leads/lead_list.html
        modified:   templates/leads/lead_update.html
        new file:   templates/navbar.html























































































































































