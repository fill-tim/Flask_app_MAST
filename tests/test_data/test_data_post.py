def test_data_post_succsess(client):
    response = (
        client.post(
            "/api/v1/data",
            json={
                "text": "test_text",
                "date": "Mon Feb 12 2024",
                "time": "11:54:50",
                "click_count": "1",
            },
        ),
    )

    assert response[0].status_code == 201
    assert response[0].json == {
        "text": "test_text",
        "date": "Mon Feb 12 2024",
        "time": "11:54:50",
        "click_count": "1",
    }


def test_data_post_failed_text_value_empty(client):
    response = (
        client.post(
            "/api/v1/data",
            json={
                "text": "",
                "date": "Mon Feb 12 2024",
                "time": "11:54:50",
                "click_count": "1",
            },
        ),
    )

    assert response[0].status_code == 400
    assert response[0].json == {"detail": "Введите текст в поле ввода!"}
