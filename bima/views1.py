def complex_operations(request):
    if request.method == 'POST':
        pilihan = request.POST['pilihan']

        if pilihan == 'custom':
            # Konversi ke bentuk √2(cos 315 degrees + i sin 315 degrees)
            result_str_custom = '√2(cos 315 degrees + i sin 315 degrees)'
            request.session['custom_conversion_result'] = result_str_custom
            context = {
                'result_str_custom': result_str_custom,
                'custom_selected': True,
            }
            return render(request, 'complex_operations.html', context)

        # Handle custom conversions
        elif pilihan in ['custom_polar', 'custom_eksponen', 'custom_kartesius']:
            custom_r = request.POST.get('custom_r', 0)
            custom_theta_degrees = request.POST.get('custom_theta', 0)
            custom_theta_radians = math.radians(float(custom_theta_degrees))
            z_custom = sp.sympify(custom_r) * (sp.cos(custom_theta_radians) + sp.I * sp.sin(custom_theta_radians))

            if pilihan == 'custom_polar':
                result_str_polar = f'{custom_r} * (cos({custom_theta_degrees} degrees) + sin({custom_theta_degrees} degrees) * I)'
                context = {
                    'result_str_polar': result_str_polar,
                    'result_str_eksponen': None,
                    'result_str_kartesius': None,
                    'custom_selected': False,
                }
            elif pilihan == 'custom_eksponen':
                result_str_eksponen = f'{custom_r} * exp({custom_theta_degrees} * I)'
                context = {
                    'result_str_polar': None,
                    'result_str_eksponen': result_str_eksponen,
                    'result_str_kartesius': None,
                    'custom_selected': False,
                }
            elif pilihan == 'custom_kartesius':
                result_str_kartesius = f'{z_custom}'
                context = {
                    'result_str_polar': None,
                    'result_str_eksponen': None,
                    'result_str_kartesius': result_str_kartesius,
                    'custom_selected': False,
                }
            return render(request, 'complex_operations.html', context)

        else:
            real_a = request.POST.get('real_a', 0)
            imag_b = request.POST.get('imag_b', 0)
            r = request.POST.get('r', 0)
            theta_degrees = request.POST.get('theta', 0)
            theta_radians = math.radians(float(theta_degrees))

            if pilihan == 'kartesius':
                # Membuat bilangan kompleks berdasarkan bagian real dan imajiner
                z = sp.sympify(real_a) + sp.I * sp.sympify(imag_b)
                result_str = f'{z}'
            elif pilihan == 'polar':
                # Konversi ke bentuk polar
                z = sp.sympify(r) * (sp.cos(theta_radians) + sp.I * sp.sin(theta_radians))
                result_str = f'{r} * (cos({theta_degrees} degrees) + sin({theta_degrees} degrees) * I)'
            elif pilihan == 'eksponen':
                # Konversi ke bentuk eksponen
                z = sp.sympify(r) * sp.exp(sp.I * theta_radians)
                result_str = f'{r} * exp({theta_degrees} * I)'
            else:
                result_str = 'Tidak ada hasil sebelumnya yang valid untuk konversi custom.'
            context = {
                'result_str': result_str,
                'result_str_custom': None,
                'result_str_polar': None,
                'result_str_eksponen': None,
                'result_str_kartesius': None,
                'custom_selected': False,
            }
            return render(request, 'complex_operations.html', context)

    return render(request, 'complex_operations.html')
