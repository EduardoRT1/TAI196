<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Usuarios Laravel</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <form action={{route('usuario.store')}} method="POST">
        @csrf
        <h1 class="display-1 mt-5 text-center text-primary">Registro de Usuario</h1>
        <h3 class="display-3 mb-5 text-center text-danger">Laravel</h3>

        <div class="container">
            @if (session('success'))
                <div class="alert alert-success" role="alert"> {{ session('success') }} </div>
            @endif

            @if (session('error'))
                <div class="alert alert-danger" role="alert"> {{ session('error') }} </div>
            @endif

            <p class="text-center">
                <a href="{{route('usuario.index')}}">Consultar Usuarios</a>
            </p>

            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" name="txtNombre" class="form-control" aria-describedby="emailHelp">
            </div>

            <div class="mb-3">
                <label for="edad" class="form-label">Edad</label>
                <input type="numbre" name="txtEdad" class="form-control" aria-describedby="emailHelp">
            </div>

            <div class="mb-3">
                <label for="correo" class="form-label">Correo</label>
                <input type="email" name="txtCorreo" class="form-control" aria-describedby="emailHelp">
            </div>

            <button type="submit" class="btn btn-primary">Guardar</button>
        </div>
        </form>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
