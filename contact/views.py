from django.views.generic import ListView, DetailView, FormView # klasy do pokazywania list i szczegolow modelu
# importuje model Author
from .models import Message
from .forms import MessageForm, ContactForm

class MessageDetailView(DetailView):
    model = Message

class MessageAddView(FormView):
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = '/'

#    def form_invalid(self, form):
#        form.save() #bo form jest instancja ModelForm ktory posiada metode seve()
#        return super(MessageAddView, self).form_valid(form)

