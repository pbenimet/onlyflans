from django import forms

class ContactFormForm(forms.Form):
    # contact_form_uuid NO SE DECLARA PUES YA TIENE VALOR POR DEFAULT,
    # heredado de la classe definida en el modelo
    customer_name   =   forms.CharField     (   label       =   'Nombre '   ,
                                                max_length  =   64          ,
                                                widget      =   forms.TextInput (attrs={
                                                                                        'class'         : 'form-control mb-3'       ,
                                                                                        'placeholder'   : 'Ingrese aquí su nombre'  ,
                                                                                                                                    }))

    customer_email  =   forms.EmailField    (   label       =   'Correo '   ,
                                                widget      =   forms.EmailInput(attrs={
                                                                                        'class'         : 'form-control mb-3'       ,
                                                                                        'placeholder'   : 'name@example.com'        ,                                                                                                                       
                                                                                                                                    }))

    message         =   forms.CharField    (    label       =   'Mensaje'   ,
                                                widget      =   forms.Textarea (attrs={
                                                                                        'class'         : 'form-control mb-3'       ,
                                                                                        'rows'          : 5        
                                                                                                                                    }))
class ContactFormModelFormForm(forms.Form):
    # contact_form_uuid NO SE DECLARA PUES YA TIENE VALOR POR DEFAULT,
    # heredado de la classe definida en el modelo
    customer_name   =   forms.CharField     (   label       =   'Nombre '   ,
                                                max_length  =   64          ,
                                                widget      =   forms.TextInput (attrs={
                                                                                        'class'         : 'form-control mb-3'       ,
                                                                                        'placeholder'   : 'Ingrese aquí su nombre'  ,
                                                                                                                                    }))

    customer_email  =   forms.EmailField    (   label       =   'Correo '   ,
                                                widget      =   forms.EmailInput(attrs={
                                                                                        'class'         : 'form-control mb-3'       ,
                                                                                        'placeholder'   : 'name@example.com'        ,                                                                                                                       
                                                                                                                                    }))

    message         =   forms.CharField    (    label       =   'Mensaje'   ,
                                                widget      =   forms.Textarea (attrs={
                                                                                        'class'         : 'form-control mb-3'       ,
                                                                                        'rows'          : 5        
                                                                                                                                    }))
