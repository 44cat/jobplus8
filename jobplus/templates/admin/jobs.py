{% extends "admin/index.html" %}
{% from "macros.html" import _render_pagination %}

{% block title %}
Admin - jobs
{% endblock %}

{% block operation %}
{% endblock %}

{% block admin %}

<table class="table text-nowrap">
    <thread>
        <tr>
            <th>ID</th>
            <th>ְλ����</th>
            <th>��ҵ����</th>
            <th>����ʱ��</th>
            <th>����״̬</th>
        </tr>
        <tbody>
            {% for jobs in pagination.items %}
            <tr>
                <td>{{ jobs.id }}</td>
                <td>{{ jobs.name }}</td>
                <td>{{ jobs.company.user.name }}</td>
                <td>{{ jobs.created_at }}</td>
                <td>
                    <div class="btn-group" role="group">
                        {% if not jos.is_disable %}
                        <a href="{{ url_for('job.disable',job_id=jobs.id) }}" type="button" class="btn btn-default">����</a>
                        {% else %}
                        <a href="{{ url_for('job.disable',job_id=jobs.id) }}" type="button" class="btn btn-default">����</a>
                        {% endif %}
                    </div>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </thread>
</table>

{{ render_pagination(pagination,'admin.jobs') }}
{% endblock %}


