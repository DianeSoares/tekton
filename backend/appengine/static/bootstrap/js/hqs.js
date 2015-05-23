$(document).ready(function () {
  var $txtInput = $('#txt-input');
  var $listaDiv = $('#lista-div');
  var $inputNome = $("input[name='nome']");
  var $ajaxImg = $('#ajax-img');
  var $hqsLista = $('#hqs-lista');

  function adicionarHq(hq) {
    var li = '<li id="li-' + hq.id + '" ><button id="btn-apagar-' + hq.id;
    li += '" class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button>';
    li += hq.nome  + '</li>';
    $hqsLista.append(li);
    $('#btn-apagar-' + hq.id).click(function () {
      $.post('/rest/hqs/apagar', {'hq_id': hq.id}, function () {
        $('#li-' + hq.id).remove();
      });
    });
  }

  $.get('/rest/hqs/listar', function (hqs) {
    $.each(hqs, function (i, hq) {
      adicionarHq(hq);
    });
  });

  $ajaxImg.hide();
  var $msgUl = $('#msg-ul');

  var $selectCategoria = $("select[name='categoria']");

  function obterInputs() {
    return {
      'nome': $inputNome.val(),
      'categoria': $selectCategoria.val()
    };
  }

  var $salvarBotao = $('#salvar-hq-btn');
  $salvarBotao.click(function () {
    $('div.has-error').removeClass('has-error');
    $('span.help-block').text('');
    $ajaxImg.fadeIn();
    $salvarBotao.attr('disabled', 'disabled');
    $.post('/rest/hqs/salvar', obterInputs(), function (hq) {
      adicionarHq(hq);
      $('input.form-control').val('');
    }).error(function (erro) {
      var errosJson = erro.responseJSON;
      for (propriedade in  errosJson) {
        $('#' + propriedade + '-div').addClass('has-error');
        $('#' + propriedade + '-span').text(errosJson[propriedade]);
      }
    }).always(function () {
      $ajaxImg.fadeOut();
      $salvarBotao.removeAttr('disabled');
    });

  });

  $('#jq').click(function fcn(evento) {
    $listaDiv.slideToggle();
  });

  $('#jq2').click(function fcn(evento) {
    $listaDiv.empty();
  });

  $('#enviar-btn').click(function () {
    var msg = $txtInput.val();
    $txtInput.val('');
    var item = '<li>' + msg + '</li>';
    $msgUl.prepend(item);
    $msgUl.fadeOut(400, function () {
      $msgUl.fadeIn(2000);
    });
  });


});