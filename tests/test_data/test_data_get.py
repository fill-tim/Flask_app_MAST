def test_data_get_succsess_in_empty_db(client):
    response = client.get("/api/v1/data")

    assert response.status_code == 200
    assert response.json == []


def test_data_get_success(client, create_data_for_test):
    response = client.get("/api/v1/data")

    assert response.status_code == 200
    assert response.json == [
        {
            "click_count": 1,
            "date": "Mon Feb 12 2024",
            "text": "test_text",
            "time": "11:54:50",
        }
    ]
