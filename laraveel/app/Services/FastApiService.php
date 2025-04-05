<?php

namespace App\Services;

use GuzzleHttp\Client;
#use GuzzleHttp\Exception\GuzzleException;
class FastApiService
{
    protected $client;
    protected $baseUri;

    public function __construct()
    {
        $this->baseUri = env('FASTAPI_URL', 'http://localhost:5001');
        $this->client = new Client([
            'base_uri' => $this->baseUri,
            'headers'  => [
                'Accept'       => 'application/json',
                'Content-Type' => 'application/json',
            ],
            'verify'  => false
        ]);
    }

    public function get($endpoint, $params = [])
    {
        try{
            $response = $this->client->get($endpoint, ['query' => $params,]);
            return json_decode($response->getBody(), true);
        } catch (\GuzzleHttp\Exception\RequestException $e) {
            return ['error'=> 'Error al conectar con el servidor'];
        }
    }

    public function post($endpoint, $data = [])
    {
        try{
            $response = $this->client->post($endpoint, ['json' => $data]);
            return json_decode($response->getBody(), true);
        } catch (\GuzzleHttp\Exception\RequestException $e) {
            return ['error'=> 'Error al conectar con el servidor'];
        }
    }

    public function put($endpoint, $data = [])
    {
        try{
            $response = $this->client->put($endpoint, ['json' => $data]);
            return json_decode($response->getBody(), true);
        } catch (\GuzzleHttp\Exception\RequestException $e) {
            return ['error'=> 'Error al conectar con el servidor'];
        }
    }

    public function delete($endpoint)
    {
        try{
            $response = $this->client->delete($endpoint);
            return json_decode($response->getBody(), true);
        } catch (\GuzzleHttp\Exception\RequestException $e) {
            return ['error'=> 'Error al conectar con el servidor'];
        }
    }

}
