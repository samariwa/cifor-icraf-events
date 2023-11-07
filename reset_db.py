#!/usr/bin/python3

from app.controllers import create
from app import app, db
app.app_context().push()


db.drop_all()


db.create_all()

#create department
department_kwargs = {
    'department': 'ICT',
}
create.create_department(**department_kwargs)

department_kwargs = {
    'department': 'PMU',
}
create.create_department(**department_kwargs)

# create staff role
staff_role_kwargs = {
    'department_id': 1,
    'role': "SuperUser",
}
create.create_staff_role(**staff_role_kwargs)

staff_role_kwargs = {
    'department_id': 2,
    'role': "Admin",
}
create.create_staff_role(**staff_role_kwargs)


# then create staff
staff_kwargs = {
    'role_id': 1, # superuser
    'first_name': "Super",
    'last_name': "User",
}
create.create_staff(**staff_kwargs)

# then create staff
staff_kwargs = {
    'role_id': 2, # admin
    'first_name': "Samuel",
    'last_name': "Mariwa",
}

create.create_staff(**staff_kwargs)


create.create_user(staff_id=1, user_status='active', email_address='superuser@cifor-icraf.org', password='3opf@mAxuU$eCujQRZQXGk#8S')
create.create_user(staff_id=2, user_status='inactive', email_address='s.mariwa@cifor-icraf.org', password='abc123')


# then create participants
participant_kwargs = {
    'department_id': 1,
    'first_name': "Samuel",
    'last_name': "Mariwa",
    'email_address': "s.mariwa@cifor-icraf.org",
}

create.create_participant(**participant_kwargs)

participant_kwargs = {
    'department_id': 2,
    'first_name': "John",
    'last_name': "Doe",
    'email_address': "j.doe@cifor-icraf.org",
}

create.create_participant(**participant_kwargs)

event_kwargs = {
    'event': "Science Week",
}

create.create_event(**event_kwargs)

event_kwargs = {
    'event': "GLF (A New Vision for Earth)",
}

create.create_event(**event_kwargs)

event_venue_kwargs = {
    'venue': "Main Conference Hall",
}

create.create_event_venue(**event_venue_kwargs)

event_venue_kwargs = {
    'venue': "Lundgren Auditorium",
}

create.create_event_venue(**event_venue_kwargs)

session_kwargs = {
    'event_id': 1,
    'event_venue_id': 1,
    'session': "Global Restoration of Mangrove Forests",
    'session_description': "Global Restoration of Mangrove Forests",
}

create.create_session(**session_kwargs)

session_kwargs = {
    'event_id': 2,
    'event_venue_id': 2,
    'session': "The Future of Forests in the Global Climate Agenda",
    'session_description': "The Future of Forests in the Global Climate Agenda",
}

create.create_session(**session_kwargs)

session_registration_kwargs = {
    'session_id': 1,
    'participant_id': 1,
}

create.create_session_registration(**session_registration_kwargs)

session_registration_kwargs = {
    'session_id': 2,
    'participant_id': 2,
}

create.create_session_registration(**session_registration_kwargs)