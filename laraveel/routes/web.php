<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;


Route::get('/', function () {
    return view('welcome');
});

Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

Route::get('/', [UserController::class, 'inicio'])->name('usuario.inicio');
Route::post('/addUser', [UserController::class, 'store'])->name('usuario.store');
Route::get('/usuarios', [UserController::class, 'index'])->name('usuario.index');
Route::get('/usuarios/{id}/edit', [UserController::class, 'edit'])->name('usuario.edit');
Route::put('/usuarios/{id}', [UserController::class, 'update'])->name('usuario.update');
Route::delete('/usuarios/{id}', [UserController::class, 'destroy'])->name('usuario.destroy');
require __DIR__.'/auth.php';
