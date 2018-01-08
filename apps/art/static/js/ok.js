$(document).ready(function () {
    $("#click").click(function () {
        $("#para1").css("color", "red");
    })

    $("#hide").click(function () {
        $("#para2").hide();
    })

    $("#show").click(function () {
        $("#para3").show();
    })

    $("#toggle").click(function () {
        $("#para4").toggle();
    })

    $("#slideDown").click(function () {
        $("#para5").slideDown("slow");
    })

    $("#slideUp").click(function () {
        $("#para6").slideUp();
    })

    $("#slideToggle").click(function () {
        $("#para7").slideToggle();
    })

    $("#fadeIn").click(function () {
        $("#para8").fadeIn();

    })

    $("#fadeOut").click(function () {
        $("#para9").fadeOut("slow");

    })

    $("#addClass").click(function () {
        $("#para10").last().addClass("color");

    })

    $("#before").click(function () {
        $("#para11").before("<b>Click Me </b>");

    })
    $("#after").click(function () {
        $("#para12").after("<b>Click Me </b>"); a
    })

    $("#Append").click(function () {
        $("#para13").append("<b>coffee </b>")

    })

    $("#html").click(function () {
        var htmlString = $("#html").html();
        $("#para14").text(htmlString);

    })
    $("#attr").click(function () {
        var title = $("em").attr("title");
        $("#para15").text(title);

    })

    $("#val").click(function () {
        var input = $("#textArea").val();
        $("#para16").text(input);

    })

    $('#nametxt').keyup(function () {
        var name = $('#nametxt').val();
        $('#areatext').text(name);
    })

    var quote = "";
    $('#copy').click(function () {
        var mes = $('#datatext').val()
        $('#datatext').data('quotes', mes);
    })

    $('#displayme').click(function () {
        alert($('#datatext').data('quotes'));
    })


    var slideIndex = 0;
    showSlides();

    function showSlides() {
        var i;
        var slides = document.getElementsByClassName("mySlides");
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > slides.length) { slideIndex = 1 }
        slides[slideIndex - 1].style.display = "block";
        setTimeout(showSlides, 2000); // Change image every 2 seconds
    }













}); 