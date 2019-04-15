$(document).ready(function () { 
    var $seuCampoCpf = $(".cpf");
    $seuCampoCpf.mask('000.000.000-00', {reverse: false});

    var $seuCampoTel = $(".telefone");
    $seuCampoTel.mask('(00) 00000-0000', {reverse: false});
});