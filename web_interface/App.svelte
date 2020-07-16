<main>
    <div class="row">
        <div class="col">
            <button type="button" class="btn btn-primary">Печать</button>
            <button type="button" class="btn btn-secondary" on:click={exportToCSV(measurements)}>Экспорт в CSV файл</button>
        </div>
    </div>
    <br>
	<form action="." method="post">
        <div class="row">
            <div class="col">
                <p>Количество строк на странице:</p>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="value" id="id50" bind:group={measurementsPerPage} value={50} on:click={sliceForPagination(page, measurements, 50)}>
                    <label class="form-check-label" for="id50">50</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="value" id="id100" bind:group={measurementsPerPage} value={100} on:click={sliceForPagination(page, measurements, 100)}>
                    <label class="form-check-label" for="id100">100</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="value" id="id150" bind:group={measurementsPerPage} value={150} on:click={sliceForPagination(page, measurements, 150)}>
                    <label class="form-check-label" for="id150">150</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="value" id="id200" bind:group={measurementsPerPage} value={200} on:click={sliceForPagination(page, measurements, 200)}>
                    <label class="form-check-label" for="id200">200</label>
                </div>
            </div>
            <div class="col">
                <p>Фильтр:</p>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="period" id="day" bind:group={checked.day} value={true} on:click={() => showRadio('day')}>
                    <label class="form-check-label" for="day">Показать за день</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="period" id="range" bind:group={checked.range} value={true} on:click={() => showRadio('range')}>
                    <label class="form-check-label" for="range">Показать за период</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="period" id="all" bind:group={checked.all} value={true} on:click={() => showRadio(undefined)}>
                    <label class="form-check-label" for="all">Все результаты</label>
                </div>
            </div>
            <div class="col">
                {#if checked.day}
                    <p>Выберите дату:</p>
                    <div class="input-group date">
                        <input type="date" class="form-control" bind:value={day_1}>
                    </div>
                    <br>
                    <button type="button" class="btn btn-primary" on:click={() => sortByDay(day_1, measurements)}>Render day</button>
                {:else if checked.range}
                    <p>Выберите диапазон:</p>
                    <div class="input-group date">
                        <p>С</p>
                        <input type="date" class="form-control" bind:value={day_1}>
                        <p>По</p>
                        <input type="date" class="form-control" bind:value={day_2}>
                    </div>
                    <br>
                    <button type="button" class="btn btn-primary" on:click={() => sortByPeriod(day_1, day_2, measurements)}>Render range</button>
                {/if}
            </div>
        </div>
    </form>
    <br>
    <div class="row">
        <div class="col">
            <div class="table-responsive">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Дата</th>
                            <th scope="col">Время</th>
                            <th scope="col">Образец</th>
                            <th scope="col">Сера</th>
                            <th scope="col">Рассеянное</th>
                            <th scope="col">Концентрация</th>
                            <th scope="col">Аналитическая программа</th>
                            <th scope="col">Оператор</th>
                        </tr>
                    </thead>
                    <tbody id="table">
                        {#each measurementsCut as item}

                            <tr>
                                <td>{ item.id }</td>
                                <td>{ item.datatime_d }</td>
                                <td>{ item.datatime_h }</td>
                                <td>{ item.obrazec }</td>
                                <td>{ item.sera }</td>
                                <td>{ item.rasseyanoe }</td>
                                <td>{ item.koncentracia }</td>
                                <td>{ item.analprog }</td>
                                <td>{ item.operator }</td>
                            </tr>

                        {/each}
                    </tbody>
                </table>
            </div>
            <div class="row">
                <div class="col">
                    <nav aria-label="Page navigation example">
                        <ul class="pagination justify-content-center">
                            {#each measurementsPages as page}
                                <li class="page-item">
                                    <button class="page-link" on:click="{() => sliceForPagination(page, measurements, measurementsPerPage, totalPages)}">
                                        {page}
                                    </button>
                                </li>
                            {/each}
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</main>
<script>
    import { onMount, onDestroy } from 'svelte';
    import Cookies from 'js-cookie/src/js.cookie.js';
	const CSRF_TOKEN = Cookies.get('csrftoken');
	const WEB_URL = getRef('web-ref');

    let measurements = [];
    let totalPages = null;
    let page = null;
    let currentPage = 1;
    let measurementsPages = [];
    let measurementsCut = [];
    let measurementsPerPage = 50;
    let checked = {day: false, range: false, all: true};
    let day_1 = '2017-05-15';
    let day_2 = '2017-06-30';

    function sortByDay(day, measurements) {
        let newMeasurements = [];
        measurements.forEach(function (measurement) {
            let day_from_measurement = new Date(measurement['datatime_d']).setHours(0,0,0,0);
            let day_from_edit = new Date(day).setHours(0,0,0,0);
            if (day_from_measurement === day_from_edit){
                newMeasurements.push(measurement);
            }
        })
        sliceForPagination(page, newMeasurements, measurementsPerPage)
    }

    function sortByPeriod(day_1, day_2, measurements) {
        let newMeasurements = [];
        measurements.forEach(function (measurement) {
            console.log('inside')
            let day_from_measurement = new Date(measurement['datatime_d']).setHours(0,0,0,0);
            let day_from_edit_1 = new Date(day_1).setHours(0,0,0,0);
            let day_from_edit_2 = new Date(day_2).setHours(0,0,0,0);
            // console.log('day_from_edit_1', day_from_edit_1)
            // console.log('day_from_edit_2', day_from_edit_2)
            // console.log('day_from_measurement', day_from_measurement)
            // if (day_from_edit_1 <= day_from_measurement <= day_from_edit_2){
            if (day_from_edit_1 <= day_from_measurement && day_from_measurement <= day_from_edit_2){
                newMeasurements.push(measurement);
                console.log('true')
            }
        })
        // console.log(newMeasurements)
        sliceForPagination(page, newMeasurements, measurementsPerPage)
    }

    function showRadio(din){
        console.log(din)
        if (din === 'day'){
            console.log('din === day')
            checked.day = true;
            checked.range = false;
            checked.all = false;
        } else if(din === 'range'){
            console.log('din === range')
            checked.day = false;
            checked.range = true;
            checked.all = false;
        } else {
            checked.day = false;
            checked.range = false;
            checked.all = true;
            sliceForPagination(page, measurements, measurementsPerPage)
        }
    }

    function createPagesArray(total){
        let arr = []
        for(let i = 1; i <= total; i++){
            arr.push(i)
        }
        return arr
    }

    function getTotalPages(length, measurementsPerPage){
        if (length % measurementsPerPage == 0){
            return length / 3
        } else {
            return length / measurementsPerPage + 1
        }
    }

    function sliceForPagination(page, measurements, measurementsPerPage, totalPages){
        if (page === null) {
            measurementsCut = measurements.slice(0, measurementsPerPage)
            console.log('null', measurementsCut)
        } else {
            measurementsCut = measurements.slice(page * measurementsPerPage - measurementsPerPage, measurementsPerPage * page)
            console.log('else', measurementsCut)
        }
    }

    function exportToCSV(measurements){
        let rows = [];
        let csvContent = "data:text/csv;charset=utf-8,\r\n";
        for (let i=0; i < measurements.length; i++) {
           let person = [ measurements[i].datatime_d,
                        measurements[i].datatime_h,
                        measurements[i].obrazec,
                        measurements[i].sera,
                        measurements[i].rasseyanoe,
                        measurements[i].koncentracia,
                        measurements[i].analprog,
                        measurements[i].operator];
           rows.push(person);
        }
        rows.forEach(function(rowArray) {
            let row = rowArray.join(",");
            csvContent += row + "\r\n";
        });

        let downloadLink = document.createElement("a");
        let blob = new Blob(["\ufeff", csvContent]);
        let url = URL.createObjectURL(blob);
        downloadLink.href = url;
        downloadLink.download = "data.csv";

        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);

        // let encodedUri = encodeURI(csvContent);
        // window.open(encodedUri, '_self');
        console.log(csvContent);
    }

    function getRef(id) {return document.getElementById(id).href;};
    onMount(async () => {
        const response = await fetch(WEB_URL, {
                                        headers: {
                                            'Accept': 'application/json, text-plain, */*',
                                            'X-Requested-With': 'XMLHttpRequest',
                                        },
        });
        let meas_json = await response.json();
        measurements = meas_json['values'];
        totalPages = getTotalPages(measurements.length, measurementsPerPage);
        measurementsPages = createPagesArray(totalPages);
        sliceForPagination(page, measurements, measurementsPerPage, totalPages);
    });
</script>
