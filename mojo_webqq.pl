#!/usr/bin/env perl
use Mojo::Webqq;
my ($qq,$host,$port,$post_api);

$qq = 3471044630;
$host = "127.0.0.1";
$port = 9292;
$post_api = 'http://127.0.0.1:2929/';

my $client = Mojo::Webqq->new(qq=>$qq);

$client->load("ShowMsg");
$client->load("Openqq", data => {
        listen=>[{host=>$host,port=>$port}],
        post_api => $post_api
    });
$client->run();
