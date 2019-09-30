class VariantHandling:
    def __variantNameConvesion__(self, variant):
        new_variant = {}
        new_variant['variantId'] = variant.pop('uniqueId')
        for key, value in variant.items():
            new_variant['v_' + key] = value
        return new_variant

    def __groupingToVariants__(self, value):
        parent = value[0]
        print(parent)
        all_variants = []
        for variant in value:
            all_variants.append(self.__variantNameConvesion__(variant))
        parent['variants'] = all_variants
        return parent

    def __run__(self, value):
        return(self.__groupingToVariants__(value))