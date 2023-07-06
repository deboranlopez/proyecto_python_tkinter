# proyecto_python_tkinter
Proyecto para la Diplomatura en Python

# Aplicación: clientes para facturar

La aplicación tiene como fin registrar clientes, cantidad de sesiones y todos los datos esenciales para facturar. Está inspirada en la dificultad que presenta para un profesional facturar por cada uno de sus clientes si no está bien organizado.

## La aplicación contiene 9 funciones:

1. Crear la base: base_debora_lopez.db

2. Crear tabla (si está creada y lo ejecutamos otra vez, tiene un “except” para que no provoque error al intentar crear otra vez la tabla)

3. Actualizar el precio de la sesión: ingresando el valor actualizado (ya que mes a mes los valores en Argentina aumentan, no sería práctico tener que borrar e ingresar mes a mes cada registro nuevamente) y apretando el botón "Precio por sesión" puede actualizar todos los totales a facturar.
Esta función cuenta con condicionales para que no pueda ingresar “0”. En este caso mostrará un error.

4. Documentos: es una función creada para auxiliar en la función de “Alta”. Devuelve una lista de los documentos que ya están en la base de datos.
 
 5. Alta: recibe como parámetros todos los datos necesarios y automáticamente calcula el “Total a facturar”. Lo actualiza en la base de datos, pero también el mismo “tree” que se muestra en pantalla.
Cuenta con condicionales que impedirán que se cargue el documento en cero o que se cargue dos veces el mismo cliente. Para no cargar el mismo documento 2 veces se lo busca en la lista que devuelve la función “Documentos”. No dejará que se dé de alta el mismo documento dos veces. Mostrará sus mensajes de error correspondientes.

6. Eliminar: se debe seleccionar en pantalla el registro a eliminar. Esta función, realiza esa tarea y actualiza la base de datos y el “tree”. En caso que no se seleccione un registro y se presione el botón para eliminar, aparecerá una advertencia para seleccionar el cliente que se desea eliminar.
Elimina todo el contenido de la lista que devolvió la función “Documentos” para que si borra un cliente, se borre de la lista y pueda ingresarlo de nuevo. Documentos volverá a crear la lista, pero actualizada sin el documento eliminado. El condicional no lo encontrará en la lista y se puede volver a dar el alta desde cero.

7. Consultar: esta función sirve para que todos los registros aparezcan en pantalla con sólo apretar el botón “Consultar todo”. Es una de las dos funciones de consultas.

8. Seleccionar: es la siguiente función de consulta, pero en este caso se realiza por “Documento”. Se coloca el documento que se desea ver en la casilla de “documento” y al seleccionar el botón “Consultar por doc”, se buscará y mostrará el registro correspondiente a ese documento.
 
9. Actualizar_treeview: se utiliza para modificar los datos en los momentos de actualización del precio y el alta.

Se colocaron los títulos, las etiquetas de entrada, las columnas del “tree”, y los botones según lo enseñado en clase, adaptándolo a la necesidad de este caso.

Contiene bucles for para recorrer los datos y poder manejar datos del “tree” (se lo especifica en la notebook).
