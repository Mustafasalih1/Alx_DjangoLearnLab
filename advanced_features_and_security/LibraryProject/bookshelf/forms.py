from django import forms

class ExampleForm(forms.Form):
    
<form method="post">
    {% csrf_token %} 
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>