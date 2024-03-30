from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        passwordHash (str): The hashed password of the user.
        email (str): The email address of the user.
        timestamp (datetime): The timestamp when the user was created.
        groups (relationship): A relationship to the groups that the user is a member of.
        messages (relationship): A relationship to the messages authored by the user.

    Methods:
        __repr__(): Returns a string representation of the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    passwordHash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, index=True, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.username}>'
    
# # association table for many-to-many relationship between users and groups
# group_members = db.Table('group_members',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
# )

# class Group(db.Model):
#     """
#     Represents a group in the application.

#     Attributes:
#         id (int): The unique identifier for the group.
#         name (str): The name of the group.
#         messages (relationship): A relationship to the messages associated with the group.
#         users (relationship): A relationship to the users who are members of the group.
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     messages = db.relationship('Message', backref='group', lazy='dynamic')
#     users = db.relationship('User', secondary=group_members, backref=db.backref('groups', lazy='dynamic'))
    
#     def __repr__(self):
#         return f'<Group {self.name}>'

class Attachment(db.Model):
    """
    Represents an attachment associated with a message.

    Attributes:
        id (int): The unique identifier for the attachment.
        file_path (str): The path to the file associated with the attachment.
        file_type (str): The type of the file associated with the attachment.
        file_name (str): The name of the file associated with the attachment.
        timestamp (datetime): The timestamp of when the attachment was created.
        message_id (int): The ID of the message that the attachment belongs to.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(128))
    file_type = db.Column(db.String(64))
    file_name = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True, default=db.func.current_timestamp())
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    
    
    def __repr__(self):
        return f'<Attachment {self.file_path}>'

class Message(db.Model):
    """
    Represents a message in the application.

    Attributes:
        id (int): The unique identifier for the message.
        body (str): The content of the message.
        timestamp (datetime): The timestamp when the message was created.
        sender_id (int): The foreign key referencing the user who sent the message.
        recipient_id (int): The foreign key referencing the user who received the message.
        isRead (bool): Indicates whether the message has been read or not.
        attachments (relationship): The attachments associated with the message.

    Methods:
        __repr__(): Returns a string representation of the message.

    """
    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    isRead = db.Column(db.Boolean, default=False)
    attachments = db.relationship('Attachment', backref='message', lazy='dynamic')

    def __repr__(self):
        return '<Message {}>'.format(self.body)