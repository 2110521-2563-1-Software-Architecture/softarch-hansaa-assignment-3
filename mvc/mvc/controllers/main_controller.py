from mvc.models.repositories.note_repository import NoteRepository

class MainController:
    def __init__(self):
        # Create note repository here
        # Your code here
        self.np = NoteRepository()
        pass
    
    def get_all_notes(self):
        # Return all notes
        # Your code here
        return self.np.get_all_notes()
        pass

    def add_note(self, note: str):
        # Add note
        # Your code here
        self.np.add_note(note)
        pass

    def clear_all(self):
        # Clear all note
        # Your code here
        self.np.clear_all_notes()
        pass
