from generated_reccomendations.recommendation_pb2 import (
    BookCategory,
    RecommendationRequest,
)
from recommendations.services import RecommendationService


def test_recommendations():
    """testing"""

    service = RecommendationService()
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=1
    )
    response = service.Recommend(request, None)
    assert len(response.recommendations) == 1
