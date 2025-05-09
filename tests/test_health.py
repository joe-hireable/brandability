def test_health_check(test_client):
    """Test that the /health endpoint returns status ok and HTTP 200."""
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
