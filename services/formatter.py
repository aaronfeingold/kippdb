class Formatter:

  def __init__(self, data):
    self.data = data
    self.formatted_messagge = self.google_sheets_formater()


  def google_sheets_formater(self):
    return self.data




