from django.contrib import admin

from .models import *

from .forms import ElegirInlineFormset

class ElegirRespuestaInline(admin.TabularInline):
	model = ElegirRespuesta
	can_delete =False
	max_num = ElegirRespuesta.MAXIMO_RESPUESTA
	min_num = ElegirRespuesta.MINIMO_RESPUESTA
	formset = ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (ElegirRespuestaInline, )
	list_display = ['texto',]
	search_fields = ['texto', 'preguntas__texto']


class PreguntasRespondidasAdmin(admin.ModelAdmin):
	list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

	class Meta:
		model = PreguntasRespondidas


admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(QuizUsuario)
admin.site.register(ComentarioUsuario)
admin.site.register(Materias)
admin.site.register(Carrera)
admin.site.register(Cuestionarios)
