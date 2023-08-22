from models.person import Person, UniqueEmailMixin
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Collaborator(Person, UniqueEmailMixin):
    __tablename__ = 'collaborator'
    username = Column(String(255))
    password = Column(String(255))
    # Relationship with Client (clients for whom the collaborator is commercial contact)
    clients = relationship("Client", back_populates="contact")
    # Relationship with Event (events for which the collaborator is support)
    events = relationship("Event", back_populates="support")
    # role = Column(Enum("administrator", "sales", "support"))
    role_id = Column(Integer, ForeignKey('role.id', ondelete="SET NULL"))
    role = relationship("Role", back_populates="collaborators")

    def detailed_view(self):
        detailed_view_string = (f"Identifiant : {self.id}"
                                f"\nName : {self.name}"
                                f"\nSurname : {self.surname}"
                                f"\nEmail : {self.email}"
                                f"\nTelephone : {self.telephone}"
                                f"\nRôle : {self.role}")
        if self.role == "Sales":
            detailed_view_string += "\nClients : "
            for client in self.clients:
                detailed_view_string += f"\n   - {client}"
        if self.role == "Support":
            detailed_view_string += "\nEvénements : "
            for event in self.events:
                detailed_view_string += f"\n   - {event}"
        return detailed_view_string
