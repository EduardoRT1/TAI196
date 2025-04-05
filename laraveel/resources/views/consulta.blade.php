<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Usuarios Laravel</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>

    <h1 class="display-5 mt-5 text-center text-primary">Consulta de Usuarios</h1>
    <h3 class="display-5 mb-5 text-center text-danger">Laravel</h3>
    <p class="text-center">
    <a href="{{ route('usuario.inicio') }}">Registrar Usuario</a>
    </p>

    <div class="container">
        @if (session('success'))
            <div class="alert alert-success" role="alert">{{ session('success') }}</div>
        @endif

        @if (session('error'))
            <div class="alert alert-danger" role="alert">{{ session('error') }}</div>
        @endif
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nombre</th>
                    <th scope="col">Edad</th>
                    <th scope="col">Correo</th>
                    <th scope="col">Acciones</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($usuarios as $usuario)
                    <tr>
                        <th scope="row">{{ $usuario['id'] }}</th>
                        <td>{{ $usuario['name'] }}</td>
                        <td>{{ $usuario['age'] }}</td>
                        <td>{{ $usuario['email'] }}</td>
                        <td>
                            <a href="{{ route('usuario.edit', $usuario['id']) }}"
                                class="btn btn-warning btn-sm">Editar</a>
                            <form action="{{ route('usuario.destroy', $usuario['id']) }}" method="POST"
                                class="d-inline">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="btn btn-danger btn-sm"
                                    onclick="return confirm('¿Estás seguro de eliminar este usuario?')">Eliminar</button>
                            </form>
                        </td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </script>
</body>

</html>
