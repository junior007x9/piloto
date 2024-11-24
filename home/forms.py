from django import forms

class ContatoForm(forms.Form):
    
    nome = forms.CharField(
        max_length=100, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 4})
    )

class FormProduto(forms.Form):
    
    nome = forms.CharField(
        max_length=100, 
        label='Nome do Produto:',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    preco = forms.DecimalField(
        max_digits=10,  # Máximo de dígitos no total (incluindo os decimais)
        decimal_places=2,  # Número de casas decimais
        label='Preço do Produto:',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'})
    )
class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome do Produto',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'})
    )
    preco = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Preço',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'})
    )