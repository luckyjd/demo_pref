
const searchPostList = (page) => {
    showLoader();
    let title_search = $("#titleSearch").val();
    let order = $("#order").val();
    let pageSize = parseInt($("#perPage").val()) ? parseInt($("#perPage").val()) : 20
    const params = {
        'page_size': pageSize
    };
    if (order) params['ordering'] = order;
    if (title_search) params['title'] = title_search;
    params['page'] = typeof (page) === 'number' ? page : 1;

    $.ajax({
        url: '/api/post',
        type: 'get',
        data: params,
        dataType: 'json',
        beforeSend: function (xhr) {
            xhr.setRequestHeader('X-CSRFToken', $.cookie("csrftoken"));
        },
        success: function (data) {
            const postList = $('#postListWrap');
            let genPost = "";
            if (data['results'].length) {
                $.each(data['results'], function (index, value) {
                    let timeAgo = moment(value['created_at']).fromNow();
                    genPost += `<div class="list-item" onclick="location.href = '/post/${value['id']}';">
                        <div>
                            <div class="d-flex justify-content-start align-self-center">
                                <i class="fa fa-user font-16 pr-1"></i>
                                <a href="#" class="item-author text-color pr-3" data-abc="true">${value['author']}</a>
                                <div class="font-italic">${timeAgo}</div>
                            </div>
                            <div class="item-except text-sm h-1x font-weight-bold">${value['title']}</div>
                            <div class="item-except text-muted text-sm h-1x">${value['comment']}</div>
                            <div class="d-flex">
                                <div class="pr-3"><span><i class="fa fa-eye font-16 pr-1"></i></span> ${value['view']}</div>
                                <div class="pr-3"><span><i class="fa fa-thumbs-o-up font-16 pr-1"></i>${value['like']}</div>
                                <div class="pr-3"><span><i class="fa fa-thumbs-o-down font-16 pr-1"></i>${value['dislike']}</div>
                                <div class="pr-3"><span><i class="fa fa-comments-o font-16 pr-1"></i>${value['total_comment']}</div>
                            </div>
                        </div>
                        <div class="ml-auto">
                            <div href="#" data-abc="true"><span class="w-64 avatar gd-warning">IMG</span></div>
                        </div>
                    </div>`
                });
                postList.html(genPost);
            } else {
                let noData = `<div class="text-center">No data</div>`;
                postList.html(noData);
            }
            renderPagination(data['count'], pageSize, data['page']);
            activatePage(data['page']);
        },
        complete: function () {
            hideLoader();
        }
    });
};

const showLoader = () => {
    $('#loader').removeClass('d-none');
};
const hideLoader = () => {
    $('#loader').addClass('d-none');
}


const activatePage = (page) => {
    $("#pagination a").removeClass("active");
    $("#pagination a[data-page='" + page + "']").addClass("active");
}
const renderPagination = (count, perPage, currentPage) => {
    let pagination = "";
    if (currentPage > 1) {
        pagination = `<li class="page-item"><a class="page-link" data-page="${currentPage - 1}"><i
                            class="fa fa-angle-left"></i></a></li>`;
    }
    let totalPages = Math.ceil(count / perPage);
    for (let i = 1; i <= totalPages; i++) {
        pagination += `<li class="page-item"><a class="page-link" data-page="${i}">${i}</a></li> `;
    }
    if (currentPage < totalPages) {
        pagination += `<li class="page-item"><a class="page-link" data-page="${currentPage + 1}"><i
                                    class="fa fa-angle-right"></i></a></li>`;
    }
    $("#pagination").html(pagination);

};

$("#pagination").on("click",".page-link" ,function () {
    let targetPage = $(this).attr("data-page");

    searchPostList(parseInt(targetPage));
});

$("#clickSearch").click(function () {
    searchPostList(1);
});

$("#order").change(function () {
    searchPostList(1);
});

$(document).ready(() => {
    searchPostList(1);
});


