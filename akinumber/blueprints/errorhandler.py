from flask import Blueprint, request


def registered_by(bp: Blueprint):
    bp.register_error_handler(Exception, handle_exception)


def handle_exception(e: Exception):
    return (
        {
            "type": "about:blank",
            "title": "Service Unavailable",
            "status": 503,
            "detail": str(e),
            "instance": request.path,
        },
        503,
        {
            "Content-Type": "application/problem+json",
        },
    )
