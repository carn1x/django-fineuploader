# -*- coding: utf-8 -*-

from django.forms.widgets import FileInput
from django.utils.safestring import mark_safe


class FineUploderWidget(FileInput):
    class Media:
        css = {'all': ('fineuploader.min.css',)}
        js = ('fineuploader.min.js',)

    def render(self, name, value, attrs=None):
        output = [super(FileInput, self).render(name, None, attrs=attrs)]
        final_attrs = self.build_attrs(attrs)
        element_id = final_attrs.get('id', None)
        output.append("""
        <div id="%(element_id)s-qq-uploader"></div>
        <script type="text/javascript">
          (function (){
            'use strict';
            var input = document.getElementById('%(element_id)s'),
                element = document.getElementById('%(element_id)s-qq-uploader'),
                endpoint = element.parentNode.attributes['action'].value,
                csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
                uploader = new qq.FineUploader({
                  element: element,
                  // autoUpload: false,
                  request: {
                    endpoint: endpoint,
                    inputName: '%(name)s',
                    customHeaders: {
                      'X-CSRFToken': csrftoken
                  }
                }
            });
            if (input) {
              input.style.display = 'none';
            }
          })();
        </script>
        """ % ({'element_id': element_id, 'name': name}))
        return mark_safe(''.join(output))
